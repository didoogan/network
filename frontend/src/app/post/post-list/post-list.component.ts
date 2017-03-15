import { Component, OnInit } from '@angular/core';
import {PostService} from "../post.service";
import {Router} from "@angular/router";
import {GeneralLib} from "../../lib";

@Component({
  selector: 'app-post-list',
  templateUrl: './post-list.component.html',
  styleUrls: ['./post-list.component.css']
})
export class PostListComponent implements OnInit {
  postList = [];
  getPostURL = "";
  _apiUrl = "";

  constructor(private _postService: PostService, private _route: Router) {
    this._apiUrl = GeneralLib.serverUrl;
    this.getPostURL = `${this._apiUrl}/post/posts/`;
    this.getPosts();
  }

  makeSympathy(post: any, sympathy: Boolean) {
    this._postService.makeSympathy(post.id, sympathy).subscribe(
      response => {
        post.likes=response.post.likes;
        post.dislikes=response.post.dislikes;
      },
      error => console.log(error)
    )
  }
  getPosts() {
    this._postService.getPosts(this.getPostURL).subscribe(
      response => this.postList = response.results,
      error => {
        console.log(error);
        this._route.navigate(['/login']);
      }
    );
  }

  ngOnInit() {
    // this._postService.getPosts().subscribe(
    //   response => this.postList = response.results,
    //   error => {
    //     console.log(error);
    //     this._route.navigate(['/login']);
    //   }
    // );
  }

}
