import { Component, OnDestroy, AfterViewChecked, ElementRef, ViewChild, ViewChildren, QueryList } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatService, ChatMessage } from './chat.service';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnDestroy, AfterViewChecked {
  messages: ChatMessage[] = [];
  input = '';
  private abortCtrl: AbortController | null = null;
  private chartsRendered = new Set<number>();

  @ViewChild('messagesRef', { read: ElementRef }) messagesRef?: ElementRef;
  @ViewChildren('chartCanvas') chartCanvases!: QueryList<ElementRef<HTMLCanvasElement>>;

  constructor(private chat: ChatService) {}

  ngOnDestroy(): void {
    this.abort();
  }

  send() {
    if (!this.input.trim()) return;
    const userPrompt = this.input.trim();
    this.messages.push({ role: 'user', content: userPrompt });
    this.input = '';
    this.startStream(userPrompt);
  }

  startStream(prompt: string) {
    this.abort();
    this.abortCtrl = new AbortController();
    this.chat.stream(prompt, this.abortCtrl.signal, (msg: ChatMessage) => {
      this.messages.push(msg);
      // allow change detection to render new nodes
    }).catch((err: unknown) => console.error(err));
  }

  abort() {
    if (this.abortCtrl) {
      this.abortCtrl.abort();
      this.abortCtrl = null;
    }
  }

  ngAfterViewChecked(): void {
    // Highlight code blocks
    try {
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-ignore
      const hljs = (window as any).hljs;
      if (!hljs) {
        import('highlight.js').then((hl) => { (window as any).hljs = hl.default || hl; this.runHighlight(); });
      } else {
        this.runHighlight();
      }
    } catch (e) {
      // ignore
    }

    // Render any pending charts
    if (this.chartCanvases && this.chartCanvases.length) {
      import('chart.js/auto').then(({ default: Chart }) => {
        this.chartCanvases.forEach((elRef) => {
          const el = elRef.nativeElement as HTMLCanvasElement;
          const idxAttr = el.getAttribute('data-msg-index');
          if (!idxAttr) return;
          const idx = Number(idxAttr);
          if (this.chartsRendered.has(idx)) return;
          const msg = this.messages[idx];
          if (!msg || msg.type !== 'chart') return;
          try {
            const cfg = msg.content as any;
            // chart.js expects {type, data, options}
            // If content already supplies type and data, use it
            const chart = new Chart(el, { type: cfg.type || 'line', data: cfg.data || cfg, options: cfg.options || {} });
            (msg as any)._chart = chart;
            this.chartsRendered.add(idx);
          } catch (e) {
            console.error('chart render error', e);
          }
        });
      }).catch(() => {});
    }
  }

  private runHighlight() {
    try {
      const blocks = document.querySelectorAll('pre code');
      const hljs = (window as any).hljs;
      blocks.forEach((b) => {
        try { hljs.highlightElement(b as HTMLElement); } catch (e) { /* ignore */ }
      });
    } catch (e) {
      // ignore
    }
  }
}
