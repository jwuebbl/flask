import { Component } from '@angular/core';

@Component({
  selector: 'app-counting-box',
  templateUrl: './counting-box.component.html',
  styleUrls: ['./counting-box.component.css']
})
export class CountingBoxComponent {
  count = 0;


  increaseCount() {
    this.count++;
  }
  
  decreaseCount() {
    this.count--;
  }
}