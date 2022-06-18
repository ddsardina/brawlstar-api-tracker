import { createContext, useReducer } from "react"
import BSReducer from "./BSReducer"

const BSContext = createContext()

export const BSProvider = ({children}) => {
    const initialState = {
        user: {},
        loading: false,
    }

    const [state, dispatch] = useReducer(BSReducer, initialState)

    // Get Search Results
    const searchUser = async (text) => {
        setLoading()

        const response = await fetch(`user/${text}`, {
            method: 'GET'
        })

        const data = await response.json()

        if (response.status === 200 || response.status === 201) {
            dispatch({
                type: 'GET_USER',
                payload: data,
            }) 
        } else {
            dispatch({
                type: 'ERROR_USER'
            })
        }
    }

    // Clear User
    const clearUser = () => dispatch({type: 'CLEAR_USER'})

    // Set Loading
    const setLoading = () => dispatch({type: 'SET_LOADING'})

    return <BSContext.Provider value={{
        user: state.user,
        loading: state.loading,
        searchUser,
        clearUser
    }}>
        {children}
    </BSContext.Provider>
}

export default BSContext