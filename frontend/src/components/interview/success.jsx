import React from "react";

class Success extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="card">
        <h1 className="center">Your Information Has Been Saved!</h1>
        <div className="center">
          <a
            href="#!"
            className="btn btn--secondary"
            onClick={() => this.props.callback()}
          >Sign Out</a>
        </div>

        <div className="center">
          <a
            href="#!"
            className="btn btn--secondary"
            onClick={() => this.props.back()}
          >Re-enter Availability</a>
        </div>
      </div>

    )
  }
}

export default Success