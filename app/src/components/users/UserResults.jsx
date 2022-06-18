import {useContext} from 'react'
import Spinner from '../layout/Spinner'
import UserItem from './UserItem'
import BSContext from '../../context/BSContext/BSContext'
import AlertContext from '../../context/AlertContext/AlertContext'

function UserResults() {
    const {user, loading, clearUser} = useContext(BSContext)
    const {setAlert} = useContext(AlertContext)

    if (!loading && user.type === 'Error') {
        setAlert('Please Enter a Valid Player ID', 'error')
        clearUser()
        return null   
    } else if (!loading && Object.keys(user).length > 0) {
        return (
            <div className='grid grid-cols-1 gap-8'>
                <UserItem key={user.id} user={user}/>
            </div>
        )
    } else if (loading) {
        return <Spinner />
    }
}

export default UserResults