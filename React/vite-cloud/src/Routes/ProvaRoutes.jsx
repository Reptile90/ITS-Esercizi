import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./Home";
import About from "./About";
import Profile from "./Profile";
import ErrorPage from "./ErrorPage";
import MyProfile from "./MyProfile";
import SingleProfile from "./SingleProfile";

const ProvaRoutes = () => {
  return (
    <BrowserRouter>
      <nav className="navbar bg-body-tertiary">
        <div className="container-fluid">
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
          <Link to="/profile">Profile</Link>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />

        {/* Rotta padre */}
        <Route path="/profile" element={<Profile />}>
          {/* Rotte figlie annidate */}
          <Route path=":id" element={<SingleProfile />} />
          <Route path="me" element={<MyProfile />} />
        </Route>

        {/* Rotta di fallback */}
        <Route path="*" element={<ErrorPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default ProvaRoutes;
