import { Injectable } from '@angular/core';

export type ChatMessage = {
  role: 'assistant' | 'user' | string;
  content: any;
  type?: string;
  rendered?: string;
};

@Injectable({ providedIn: 'root' })
export class ChatService {
  private base = (window.location.hostname === 'localhost') ? 'http://localhost:8000' : '';

  async stream(prompt: string, signal: AbortSignal | null, onMessage: (m: ChatMessage) => void) {
    const url = new URL(this.base + '/chat/stream');
    url.searchParams.set('prompt', prompt);
    const resp = await fetch(url.toString(), { signal });
    if (!resp.body) throw new Error('No response body');

    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buf = '';
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buf += decoder.decode(value, { stream: true });
      let idx;
      while ((idx = buf.indexOf('\n')) >= 0) {
        const line = buf.slice(0, idx).trim();
        buf = buf.slice(idx + 1);
        if (!line) continue;
        try {
          const obj = JSON.parse(line);
          const msg = { role: obj.type === 'text' || obj.type === 'markdown' || obj.type === 'chart' ? 'assistant' : 'assistant', content: obj.content, type: obj.type } as any;
          // prepare rendered HTML for markdown and sanitize
          if (obj.type === 'markdown') {
            // lazy import marked and DOMPurify to avoid blocking
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            const { marked } = await import('marked');
            const DOMPurify = (await import('dompurify')).default;
            const raw = marked(obj.content || '');
            msg.rendered = DOMPurify.sanitize(raw);
          }
          onMessage(msg);
        } catch (e) {
          console.error('stream parse error', e, line);
        }
      }
    }
  }
}
