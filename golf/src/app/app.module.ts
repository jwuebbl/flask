import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PersonComponent } from './person/person.component';
import { CountingBoxComponent } from './counting-box/counting-box.component';
import { AddNewPlayerButtonComponent } from './add-new-player-button/add-new-player-button.component';

@NgModule({
  declarations: [
    AppComponent,
    PersonComponent,
    CountingBoxComponent,
    AddNewPlayerButtonComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }