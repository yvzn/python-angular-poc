import { Component, inject, OnInit } from '@angular/core';
import { AboutService } from '../about-service';
import { JsonPipe } from '@angular/common';

@Component({
  selector: 'app-about-page',
  imports: [JsonPipe],
  templateUrl: './about-page.html',
})
export class AboutPage {
  private aboutService = inject(AboutService);

  aboutInfo = this.aboutService.aboutInfo;
}
