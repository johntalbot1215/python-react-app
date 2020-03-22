import React from 'react';
import { runInNewContext } from 'vm';

class NewAccount extends React.Component {

    handleSubmit = (e :React.FormEvent<HTMLFormElement>)=>{
        e.preventDefault()
        fetch('/new-account',{
            method:'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.state)
        })
    }

    handleChange = (e :React.FormEvent<HTMLInputElement>) => {
        this.setState({
            ...this.state,
            [e.currentTarget.name]: e.currentTarget.value,
        })
    }
    
    render(){
        console.log(this.state)
        return (
            <form onSubmit={this.handleSubmit}>
                <div>
                    <label>Username:</label>
                    <input type='text' name='username' onChange={this.handleChange} />
                </div>
                <div>
                    <label>Password:</label>
                    <input type='text' name='password' onChange={this.handleChange} />
                </div>
                <input type='submit'/>
            </form>
        )
    }
}

export default NewAccount;