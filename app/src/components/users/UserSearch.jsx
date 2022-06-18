import {useState, useContext} from 'react'
import BSContext from '../../context/BSContext/BSContext'
import AlertContext from '../../context/AlertContext/AlertContext'

function UserSearch() {
    const [text, setText] = useState('')

    const {user, searchUser, clearUser} = useContext(BSContext)
    const {setAlert} = useContext(AlertContext)

    const handleChange = (e) => setText(e.target.value)

    const handleSubmit = (e) => {
        e.preventDefault()

        if(text[0] === '#' ) {
            setAlert('Please Enter Your Player ID Without the Beginning #', 'error')
        } else if (text.length !== 8) {
            setAlert('Please Enter a Valid Player ID', 'error')
        } else {
            searchUser(text)

            setText('')
        }
    }

    return (
        <div className='grid grid-cols-1 xl:grid-cols-2 lg:grid-cols-2 md:grid-cols-2 mb-8 gap-8'>
        <div>
            <form onSubmit={handleSubmit}>
            <div className='form-control'>
                <div className='relative'>
                <input
                    type='text'
                    className='w-full pr-40 bg-gray-200 input input-lg text-black'
                    placeholder='Search'
                    value={text}
                    onChange={handleChange}
                />
                <button
                    type='submit'
                    className='absolute top-0 right-0 rounded-l-none w-36 btn btn-lg'
                >
                    Go
                </button>
                </div>
            </div>
            </form>
        </div>
            {Object.keys(user).length > 0 && (
               <div>
               <button
                   className='btn btn-ghost btn-lg'
                   onClick={clearUser}
               >
                   Clear
               </button>
               </div> 
            )}
        </div>
    )
}

export default UserSearch