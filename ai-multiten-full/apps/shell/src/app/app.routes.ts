import { Routes } from '@angular/router';
import { DashboardComponent } from './dashboard.component';

export const appRoutes: Routes = [
	{ path: '', loadComponent: () => import('./dashboard.component').then(m => m.DashboardComponent) },
	{ path: '**', redirectTo: '' }
];
