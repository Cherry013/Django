import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddTutorialComponent } from './components/add-tutorial/add-tutorial.component';
import { TutorialDetailsComponent } from './components/tutorial-details/tutorial-details.component';
import { TutorialListComponent } from './components/tutorial-list/tutorial-list.component';

const routes: Routes = [
  {  path: '', redirectTo: 'tutorial', pathMatch:'full'},
  { path: 'tutorial', component:TutorialListComponent },
  { path: 'tutorial/:id', component:TutorialDetailsComponent },
  { path: 'add', component:AddTutorialComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
