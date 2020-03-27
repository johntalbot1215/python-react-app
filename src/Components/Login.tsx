import React from 'react'
class Login extends React.Component{
    onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        fetch("/login", {
            method: "POST",
            body: JSON.stringify(this.state),
            headers:{
                "Content-type": "application/json",
                "Accept": "application/json"
            }
        })
    }
    inputChanged = (e :React.FormEvent<HTMLInputElement>) => {
        this.setState({
            ...this.state,
            [e.currentTarget.name]: e.currentTarget.value
        })
    }
    render(){
        return (
            <form onSubmit={this.onSubmit}>
                <div>
                    <label>Username</label>
                    <input type="text" name="username" onChange={this.inputChanged} />
                </div>
                <div>
                    <label>Password</label>
                    <input type="text" name="password" onChange={this.inputChanged} />
                </div>
                <input type="submit"/>
            </form>
        )
    }
}
export default Login;