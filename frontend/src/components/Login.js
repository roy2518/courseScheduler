import React from 'react'
import {Grid, Header, Segment, Form} from 'semantic-ui-react'
import {Redirect} from 'react-router-dom'


class Login extends React.Component {

    state = {
        netid: '',
        redirect: false,
        invalidLoginError: null
    }

    handleSubmit = () => {
        if (this.state.netid == '') {
            this.setState({invalidLoginError: {content: 'Please enter a valid netid', pointing: 'below'}})
            return
        } else {
            this.setState({invalidLoginError: null})
        }
        this.props.setNetID(this.state.netid)
        this.setState({redirect: true})
    }

    render() {

        if(this.state.redirect){
            return <Redirect push to= "/" />
        }

        return (
            <Grid textAlign='center' style={{ height: '100vh' }} verticalAlign='middle' centered>
                <Grid.Column style={{ maxWidth: 450 }}>
                    <Header color='grey' textAlign='center' style={{ fontSize: "60px", letterSpacing: "4.8px" }}>
                        Course Scheduler
                    </Header>
                    <Header as='h4' color='grey' textAlign='center'>
                        Please Enter Your NetID
                    </Header>
                    <Segment clearing raised style={{ borderColor: "white" }}>
                        <Form size='mini' onSubmit={this.handleSubmit}>
                            <Form.Input
                                fluid
                                placeholder='netid'
                                value={this.state.netid}
                                error={this.state.invalidLoginError}  
                                onChange={(e) => this.setState({netid: e.target.value})}
                            />
                            <Form.Button color='violet' size='small' fluid>
                                Enter
                            </Form.Button>

                        </Form>

                    </Segment>
                </Grid.Column>
            </Grid>
        )
    }
}
export default Login;