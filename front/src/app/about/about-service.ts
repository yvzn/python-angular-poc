import { httpResource } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AboutService {
    aboutInfo = httpResource(() => `/api/about`);
}
