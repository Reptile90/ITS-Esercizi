import React from 'react'

const PostList = ({posts}) => {
  return (
    <div>
      <h2 className="mb-3"> Post pubblicati</h2>
      {posts.length === 0 ? (
        <div className="alert alert-info">Devi pubblicare un post!</div>
      ) : (
        posts.map((post, index) => (
          <div key={index} className="card mb-3">
            <div className="card-body">
              <h5 className="card-title">{post.titolo}</h5>
              <p className="card-text">{post.contenuto}</p>
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default PostList