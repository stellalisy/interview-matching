import React from "react";

class UserInfo extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="card">
        <h1 className="center">Your Info</h1>
        <p>
          <strong>Name:</strong> {this.props.name}<br />
          <strong>Email:</strong> {this.props.email}<br />
          <strong>Role:</strong> {this.props.role}
        </p>
        <div className="center">
          <br />
          <a href="#!" onClick={() => this.props.callback()} className="btn btn--secondary">Sign Out</a>
        </div>
      </div>
    )
  }
}

export default UserInfo