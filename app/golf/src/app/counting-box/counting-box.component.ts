import { Component } from '@angular/core';

@Component({
  selector: 'app-counting-box',
  templateUrl: './counting-box.component.html',
  styleUrls: ['./counting-box.component.css']
})
export class CountingBoxComponent {
  count = 0;
  handleClick() {
    this.count++;
    console.log(this.count)
  }
}
