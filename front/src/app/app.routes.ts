import { Routes } from '@angular/router';
import { AboutPage } from './about/about-page/about-page';
import { HomePage } from './home/home-page/home-page';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    component: HomePage,
  },
  {
    path: 'about',
    component: AboutPage
  }
];
