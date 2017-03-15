import { Component, OnInit } from '@angular/core';
import {PostService} from "../post.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-post-list',
  templateUrl: './post-list.component.html',
  styleUrls: ['./post-list.component.css']
})
export class PostListComponent implements OnInit {
  postList = [];

  constructor(private _postService: PostService, private _route: Router) { }

  makeSympaty(post: any, sympathy: Boolean) {
    this._postService.makeSympathy(post.id, sympathy).subscribe(
      response => {
        post.likes=response.post.likes;
        post.dislikes=response.post.dislikes;
      },
      error => console.log(error)
    )
  }

  ngOnInit() {
    this._postService.getPosts().subscribe(
      response => this.postList = response,
      error => {
        console.log(error);
        this._route.navigate(['/login']);
      }
    );
  }

}
