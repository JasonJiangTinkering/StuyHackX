import React, { Component } from "react"

const UserContext = React.createContext();

const UserProvider = UserContext.Provider;

const data = {
	isSignedIn: false,
	firstName: "",
	lastName: ""
};

class UserContextProvider extends Component {
  render() {
    return (
      <UserProvider value={data}>{this.props.children}</UserProvider>
    )
  }
}

export { UserContext, UserContextProvider }
