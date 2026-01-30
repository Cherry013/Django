import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, catchError, switchMap, throwError } from 'rxjs';
import { AuthService } from '../services/auth.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(private authService:AuthService) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    const req = request.clone({
      setHeaders: {
        Authorization: `Bearer ${this.authService.accessToken}`
      }
    });

    return next.handle(req).pipe(catchError((err: HttpErrorResponse) => {
      console.log(err.status);
      if (err.status === 403) {
        this.authService.refresh().pipe(
          switchMap((res: any) => {
            this.authService.accessToken = res.token;

            return next.handle(request.clone({
              setHeaders: {
                Authorization: `Bearer ${this.authService.accessToken}`
              }
            }));
          })
        );
      }

      return throwError(() => err);

    }));
  }
}
