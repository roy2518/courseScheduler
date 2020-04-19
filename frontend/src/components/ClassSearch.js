import React, { Fragment } from 'react'
import {Form, Segment, Button} from 'semantic-ui-react'
import {client} from '../constants/api'
import CourseGroup from './CourseGroup'

class ClassSearch extends React.Component {

    state = {
        searchTerm: '',
        searchResults: null,
        courseGroups: {},
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

        let response = await client.get(`/courseoff/?subject=${this.state.searchTerm}`)
        if (response.status % 200 > 100) {
            throw('error')
        }

        this.setState({courseGroups: {}})
        let courses = response.data
        courses.forEach((course) => {
            if (this.state.courseGroups[`${course.subject} ${course.course_num}`] == null) {
                this.state.courseGroups[`${course.subject} ${course.course_num}`] = [course]
            } else {
                this.state.courseGroups[`${course.subject} ${course.course_num}`].push(course)
            }
        })


        this.setState({searchResults: response.data})
        console.log(this.state.searchResults)
    }

    renderResults = (results) => {

        if (Object.keys(results).length === 0 ) {
            return <div>No results found</div>
        }

        if (results.length === 0) {
            return <div>No results found</div>
        }

        return (
            Object.entries(results).map((course) => {

            
                return (
                <Segment>
                    {course[0]}
                    <CourseGroup 
                        courseName={course[0]}
                        courseOfferings={course[1]} 
                        trigger={<Button floated='right'>Expand</Button>}
                        addCourse={this.props.addCourse}
                        />
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
                    {this.renderResults(this.state.courseGroups)}
                </Segment>
            </Fragment>
            
        )
    }

}


export default ClassSearch