import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

interface UseCase {
  id: string;
  name: string;
  description?: string;
}

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent {
  tenantId = 'demo_tenant';
  useCases: UseCase[] = [
    { id: 'summarize', name: 'Summarize', description: 'Summarize text or documents' },
    { id: 'chart', name: 'Generate Chart', description: 'Produce demo chart data' },
    { id: 'code', name: 'Code Assistant', description: 'Code examples and snippets' }
  ];

  openChat(useCase: UseCase) {
    const params = new URLSearchParams({ tenant: this.tenantId, use_case: useCase.id, user: 'demo_user' });
    // Open chat app (remote or standalone) with context in query string
    window.location.href = `http://localhost:4201/?${params.toString()}`;
  }
}
