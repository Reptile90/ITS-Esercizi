import React, { useState } from 'react'
import PostForm from './PostForm';
import PostList from './PostList';

const BlogApp = () => {

    const [posts, setPosts] = useState([]);

    const aggiungiPost = (nuovoPost) => {
        setPosts([...posts, nuovoPost]);

    }
    return (
        <div className="container mt-5">
            <h1 className="text-center mb-4"> Il Mio Blog</h1>
            <PostForm aggiungiPost={aggiungiPost} />
            <PostList posts={posts} />
        </div>
    );
};

export default BlogApp