import React from "react";

class Success extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="card">
        <h2 className="center">Your Information Has Been Saved!</h2>
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