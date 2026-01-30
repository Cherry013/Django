import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

const baseUrl = 'http://localhost:8000/api';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  accessToken = '';

  constructor(private http:HttpClient) { }

  register(body: any) {
    return this.http.post(`${baseUrl}/register`, body);
  }

  login(body: any) {
    return this.http.post(`${baseUrl}/login`, body, {withCredentials: true});
  }

  user() {
    return this.http.get(`${baseUrl}/user`);
  }

  refresh() {
    return this.http.post(`${baseUrl}/refresh`, {}, {withCredentials: true});
  }

}
