import React from 'react';
import { Link } from 'react-router-dom';

class MainPage extends React.Component {
    render() {
        return (
            <div className='App'>
                <header className='App-header'>
                    Employee Time System
                </header>
                <Link to="new-account">
                    <button className="Login-button">
                        New Account
                    </button>
                </Link>
            </div>
        )
    }
}

export default MainPage;