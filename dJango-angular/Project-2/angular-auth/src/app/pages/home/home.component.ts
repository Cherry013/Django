import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  messege = '';

  constructor(private authSevice:AuthService) {}

  ngOnInit(): void {
    this.authSevice.user().subscribe({
      next: (res: any) => { this.messege = `hii ${res.first_name} ${res.last_name}` },
      error: err => { this.messege = `You are not Authenticated` }
    });
  
  }

}
