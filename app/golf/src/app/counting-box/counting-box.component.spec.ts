import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CountingBoxComponent } from './counting-box.component';

describe('CountingBoxComponent', () => {
  let component: CountingBoxComponent;
  let fixture: ComponentFixture<CountingBoxComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CountingBoxComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CountingBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
