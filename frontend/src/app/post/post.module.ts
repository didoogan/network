import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PostListComponent } from './post-list/post-list.component';
import {PostService} from "./post.service";
import {RouterModule} from "@angular/router";

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild([
      { path: "post-list", component: PostListComponent }
    ])
  ],
  declarations: [PostListComponent],
  providers: [
    PostService
  ]
})
export class PostModule { }
