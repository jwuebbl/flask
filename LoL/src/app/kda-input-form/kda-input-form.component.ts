import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-kda-input-form',
  templateUrl: './kda-input-form.component.html',
  styleUrls: ['./kda-input-form.component.css']
})
export class KdaInputFormComponent {
  constructor(private http: HttpClient) {}
  char: string = "";
  kills: number = 0;
  deaths: number = 0;
  assists: number = 0;
  numOfAttempts: number = 0;

  resetAllFields() {
    this.char = "";
    this.kills = 0;
    this.deaths = 0;
    this.assists = 0;
    this.numOfAttempts = 0;
    (<HTMLInputElement>document.getElementById("kills")).style.backgroundColor = "White";
    (<HTMLInputElement>document.getElementById("deaths")).style.backgroundColor = "White";
    (<HTMLInputElement>document.getElementById("assists")).style.backgroundColor = "White";
    (<HTMLInputElement>document.getElementById("char")).style.backgroundColor = "White";
  }

  kdaSubmit() {
    if (this.char == "") {
        (<HTMLInputElement>document.getElementById("char")).style.backgroundColor = "Red";
    } else if (this.kills < 0) {
        (<HTMLInputElement>document.getElementById("kills")).style.backgroundColor = "Red";
    } else if (this.deaths < 0) {
        (<HTMLInputElement>document.getElementById("deaths")).style.backgroundColor = "Red";
    } else if (this.assists < 0) {
        (<HTMLInputElement>document.getElementById("assists")).style.backgroundColor = "Red";
    } else {
        const observer = {
          next: (response: any) => {
            console.log('POST request successful:', response);
            this.resetAllFields();
          },
          error: (error: any) => {
            console.log('POST request error:', error);
            this.numOfAttempts++;
            (<HTMLInputElement>document.getElementById("errorMessage")).innerText = "There was an error POSTing the data. Please try again. Number of attempts: " + this.numOfAttempts;
          }
        };
        var data = {
        char: this.char,
        kills: this.kills,
        deaths: this.deaths,
        assists: this.assists
        };
        this.http.post('http://localhost:80/submitLeagueGame', data).subscribe(observer);
    } 
  }
}
