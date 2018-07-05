import 'bootstrap/dist/css/bootstrap.min.css';

import React from 'react';
import GoTrashcan from 'react-icons/lib/go/trashcan';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {events: [],
                  isLoading: false,
                  error: null};

    this.loadEventsFromDatabase = this.loadEventsFromDatabase.bind(this);
  }

  loadEventsFromDatabase() {
    fetch(this.props.url)
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Something went wrong ...');
        }
      })
      .then(data => this.setState({ events: data, isLoading: false }))
      .catch(error => this.setState({ error, isLoading: false }));
  }

  componentDidMount() {
    this.setState({ isLoading: true });
    this.loadEventsFromDatabase();
  }

  render() {
    const { events, isLoading, error } = this.state;
    return (
      <div className>
        <AddForm kinds={this.props.kinds} url={this.props.url} updateCallback={this.loadEventsFromDatabase} />
        <table className="table table-striped">
            <thead>
            <tr>
              <th>Date</th>
              <th>Kind</th>
              <th>Comment</th>
              <th></th>
            </tr>
            </thead>
            <tbody>
              <Events events={events} error={error} isLoading={isLoading} url={this.props.url} updateCallback={this.loadEventsFromDatabase}/>
            </tbody>
          </table>
      </div> 
    )
  }
}

class AddForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {comment: '', time: new Date().toString(),  kind: props.kinds[0][0]};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  // This is a managed-state input form, so this method keeps the internal
  // state in sync with the contents of the form on the page.
  handleChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    // call add API and then call update callback
    console.log('A new comment was submitted: ' + this.state);
    fetch(this.props.url,
      { method: 'POST',
        body: JSON.stringify(this.state)
      })
    .then(response => this.props.updateCallback())
    .catch(error => console.log('Fetch Error =\n', error))
  }

  render() {
    const { kinds } = this.props;
    return (
      <form onSubmit={this.handleSubmit} className="form-inline pt-2 pb-2">
        <div className="col-sm-4 form-group">
          <label for="comment1">Comment:</label>
          <input
            id="comment1"
            name="comment"
            type="text"
            value={this.state.comment}
            onChange={this.handleChange} />
        </div>
        <div className="col-sm-3 form-group">
          <label for="time1">Date:</label>
          <input
            id="time1"
            name="time"
            type="text"
            value={this.state.time}
            onChange={this.handleChange} />
        </div>
        <div className="col-sm-3 form-group">
          <label for="kind1">Kind:</label>
          <select value={this.state.kind}
            id="kind1"
            name="kind"
            type="text"
            value={this.state.kind}
            onChange={this.handleChange}>
            {kinds.map((kind) => <option key={kind[0]} value={kind[0]}>{kind[1]}</option>)}
          </select>
        </div>
        <input type="submit" className=" col-sm-2 btn btn-primary" value="Add" />
      </form>
    );
  }
}

class Events extends React.Component {
  render() {
    const { events, isLoading, error } = this.props;
    if (error) {
        return <p>{error.message}</p>;
    }
    if (isLoading) {
      return <tr><td colSpan="4">Loading...</td></tr>;
    }
    return events.map((event) => <Event key={event.id} id={event.id} info={event} url={this.props.url} updateCallback={this.props.updateCallback} />)
  }
}

class Event extends React.Component {
  constructor(props) {
    super(props);
    this.deleteThis = this.deleteThis.bind(this);
  }

  render() {
    const info = this.props.info
    return <tr>
            <td>{info.time}</td>
            <td>{info.name}</td>
            <td>{info.comment}</td>
            <td><button className="btn btn-link" onClick={this.deleteThis}><GoTrashcan /></button></td>
          </tr>
  }

  deleteThis(page_event) {
    console.log('Deleting event ', this.props.id);
    fetch(this.props.url + 'event/' + this.props.id,
      { method: 'DELETE' })
    .then(response => this.props.updateCallback())
    .catch(error => console.log('Delete error =\n', error))
  }
}

module.exports = {App: App}
