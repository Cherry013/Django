import { Component, OnInit } from '@angular/core';
import { Tutorial } from 'src/app/models/tutorial.model';
import {  TutorialService } from 'src/app/services/tutorial.service';


@Component({
  selector: 'app-tutorial-list',
  templateUrl: './tutorial-list.component.html',
  styleUrls: ['./tutorial-list.component.css']
})
export class TutorialListComponent implements OnInit {
constructor(private tutorialService: TutorialService){}

  ngOnInit(): void {
  }

  tutorial?: Tutorial[];
  currentTutorial: Tutorial = {
  };
  currentIndex = -1;
  title: string='';

  retrieveTutorial(): void {
    this.tutorialService.getAll()
    .subscribe({
      next:(data) => {
        this.tutorial = data;
        console.log(data);
      },
      error: (e) => console.log(e)
    });
  }

  refreshList(): void {
    this.retrieveTutorial();
    this.currentTutorial = {};
    this.currentIndex = -1;
  }

  setActiveTutorial(tutorial: Tutorial, index: number): void {
    this.currentTutorial = tutorial;
    this.currentIndex = index;
  }

  removeAllTutorials(): void {
    this.tutorialService.deleteAll()
    .subscribe({
      next: (res) => {
        console.log(res);
        this.refreshList();
      },
      error: (e) => console.log(e)
    })
  }

  searchTitle(): void {
    this.currentTutorial = {};
    this.currentIndex = -1;

    this.tutorialService.findByTitle(this.title)
    .subscribe({
      next: (data) => {
        this.tutorial = data;
        console.log(data);
      },
      error: (e) => console.log(e)
    });
  }
  

}
