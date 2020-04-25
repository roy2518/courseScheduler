import React, { Fragment } from 'react'
import { Form, Segment, Button } from 'semantic-ui-react'
import { client } from '../constants/api'
import CourseGroup from './CourseGroup'
import SearchBar from './SearchBar'

class ClassSearch extends React.Component {

    state = {
        searchTerm: '',
        searchValues: [''],
        searchBars: [0],
        searchResults: null,
        courseGroups: {},
        invalidSearchError: null
    }

    handleSearchChange = (index, filterType, value) => {
        let preSearchValues = this.state.searchValues
        preSearchValues[index] = {filterType: filterType, value: value}
        this.setState({ searchValues: preSearchValues })
    }

    addSearchBar = () => {
        let preSearchBars = this.state.searchBars
        let preSearchValues = this.state.searchValues
        preSearchBars.push(Date.now())
        preSearchValues.push(null)
        this.setState({ searchBars: preSearchBars, searchValues: preSearchValues })
    }

    removeSearchBar = (index) => {
        console.log(index)
        let preSearchBars = this.state.searchBars
        let preSearchValues = this.state.searchValues
        preSearchBars.splice(index, 1)
        preSearchValues.splice(index, 1)
        this.setState({ searchBars: preSearchBars, searchValues: preSearchValues })
    }

    buildQuery = () => {
        let query = '?'

        this.state.searchValues.forEach((searchValue) => {

            if (searchValue === null) {
                return
            }

            if (searchValue.filterType === 'subject' || searchValue.filterType === 'professor') {
                query = query.concat(`${searchValue.filterType}=${searchValue.value}&`)
            } else if (searchValue.filterType === 'course-num') {
                query = query.concat(`course_num=${searchValue.value}&`)
            } else if (searchValue.filterType === 'start-time') {
                if (searchValue.value.after !== null) {
                    query = query.concat(`afterstart=${searchValue.value.after}&`)
                }
                if (searchValue.value.before !== null) {
                    query = query.concat(`beforestart=${searchValue.value.before}&`)
                } 
            } else if (searchValue.filterType === 'end-time') {
                if (searchValue.value.after !== null) {
                    query = query.concat(`afterend=${searchValue.value.after}&`)
                }
                if (searchValue.value.before !== null) {
                    query = query.concat(`beforeend=${searchValue.value.before}&`)
                } 
            } else if (searchValue.filterType === 'attributes') {
                for (let attr of searchValue.value) {
                    query = query.concat(`${attr}=T&`)
                }
            } else if (searchValue.filterType === 'days') {
                for (let day in searchValue.value) {
                    if (searchValue.value[day] !== null) {
                        query = query.concat(`${day}=${searchValue.value[day]}&`)
                    }
                }    
            }
        })

        return query
    }

    onFormSubmit = async (event) => {
        event.preventDefault();

        let response = await client.get(`/courseoff/${this.buildQuery()}`)
        if (response.status % 200 > 100) {
            throw ('error')
        }

        this.setState({ courseGroups: {} })
        let courses = response.data
        courses.forEach((course) => {
            if (this.state.courseGroups[`${course.subject} ${course.course_num}`] == null) {
                this.state.courseGroups[`${course.subject} ${course.course_num}`] = [course]
            } else {
                this.state.courseGroups[`${course.subject} ${course.course_num}`].push(course)
            }
        })


        this.setState({ searchResults: response.data })
        console.log(this.state.searchResults)
    }





    renderSearchBars = (searchBars) => {
        return (
            searchBars.map((searchBar, index) =>
                <Form.Group key={searchBar} inline>
                    <SearchBar handleChange={this.handleSearchChange.bind(this, index)} />
                    <Button circular icon='minus' type='button' onClick={(e) => { e.preventDefault(); this.removeSearchBar(index) }} />
                </Form.Group>
            )
        )

    }

    renderResults = (results) => {

        if (Object.keys(results).length === 0) {
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
                    {this.renderSearchBars(this.state.searchBars)}
                    <Button circular icon='plus' type='button' onClick={(e) => { e.preventDefault(); this.addSearchBar() }} />
                    <Button floated='right' icon='search'>Search</Button>
                </Form>
                <Segment style={{ overflow: 'auto', maxHeight: '75vh' }}>
                    {this.renderResults(this.state.courseGroups)}
                </Segment>
            </Fragment>

        )
    }

}


export default ClassSearch