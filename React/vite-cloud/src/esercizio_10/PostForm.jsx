import React, { useState } from 'react'

const PostForm = ({aggiungiPost}) => {
    const [titolo,setTitolo] = useState ("");
    const [contenuto, setContenuto] = useState ("");

    const handleSubmit = (e) => {
  e.preventDefault();
  if (titolo && contenuto) {
    const nuovoPost = {
      titolo,
      contenuto,
    };
    aggiungiPost(nuovoPost);
    setTitolo("");
    setContenuto("");
  } else {
    alert("Riempi il form");
  }
};

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <h2 className="mb-3"> Nuovo Post</h2>
      <div className="mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Titolo"
          value={titolo}
          onChange={(e) => setTitolo(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <textarea
          className="form-control"
          placeholder="Contenuto"
          rows="4"
          value={contenuto}
          onChange={(e) => setContenuto(e.target.value)}
        />
      </div>
      <button type="submit" className="btn btn-primary">Pubblica</button>
    </form>
  );
};

export default PostForm