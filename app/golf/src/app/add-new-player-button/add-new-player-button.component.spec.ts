import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddNewPlayerButtonComponent } from './add-new-player-button.component';

describe('AddNewPlayerButtonComponent', () => {
  let component: AddNewPlayerButtonComponent;
  let fixture: ComponentFixture<AddNewPlayerButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddNewPlayerButtonComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddNewPlayerButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
