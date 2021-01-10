import React from "react";

const UserContext = React.createContext({
  signedIn: false,
	firstName: "",
	lastName: "",
	email: "",
	picture: ""
});

export default UserContext
