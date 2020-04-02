import React, { Fragment } from 'react'
import {Form, Segment, Button} from 'semantic-ui-react'
import {client} from '../constants/api'

class ClassSearch extends React.Component {

    state = {
        searchTerm: '',
        searchResults: null,
        invalidSearchError: null 
    }

    onFormSubmit = async(event) => {
        event.preventDefault();
        if (this.state.searchTerm == '') {
            this.setState({invalidSearchError: {content: 'Please enter a search term'}})
            return
        } else {
            this.setState({invalidSearchError: null})
        }

        let response = await client.get(`/${this.state.searchTerm}`)
        if (response.status % 200 > 100) {
            throw('error')
        }

        this.setState({searchResults: response.data})
        console.log(this.state.searchResults)
    }

    renderResults = (results) => {

        if (results == null) {
            return <div>Search for a class here!</div>
        }

        if (results.length === 0) {
            return <div>No results found</div>
        }

        console.log(results)
        return (
            results.map((course) => {

                let days = ''
                if (course.days.mon === true) {
                    days = days.concat('M')
                }
                if (course.days.tues === true) {
                    days = days.concat('T')
                }
                if (course.days.wed === true) {
                    days = days.concat('W')
                }
                if (course.days.thur === true) {
                    days = days.concat('Th')
                }
                if (course.days.fri === true) {
                    days = days.concat('F')
                }

                return (
                <Segment key={[course.subject, course.course_num, course.type, course.id]} course={course}>
                    {course.subject} {course.course_num} / {course.type} ({course.start_time}-{course.end_time} {days}) 
                    <Button floated='right' onClick={(e, {course}) => {this.props.addCourse(course)}}>Add</Button>
                </Segment>
                )
            })
        )
    }

    render() {
        return (
            <Fragment>
                <Form onSubmit={this.onFormSubmit}>
                <Form.Input 
                    type='text'
                    icon='search'
                    value={this.state.searchTerm}
                    onChange={(e) => this.setState({searchTerm: e.target.value.toUpperCase()})}
                    error={this.state.invalidSearchError}    
                />
                </Form>
                <Segment  style={{overflow: 'auto', maxHeight: "85vh"}}>
                    {this.renderResults(this.state.searchResults)}
                </Segment>
            </Fragment>
            
        )
    }

}


export default ClassSearch