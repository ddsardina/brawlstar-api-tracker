import { Link } from 'react-router-dom'
import PropTypes from 'prop-types'
import {FaStar} from 'react-icons/fa'

function UserItem({ user: {name, playertag} }) {
    return (
        <div className='card shadow-md compact side bg-base-100'>
          <div className='flex-row items-center space-x-4 card-body'>
            <div>
              <div className='avatar'>
                <FaStar className='rounded-full shadow w-12 h-12'/>
              </div>
            </div>
            <div>
              <h2 className='card-title'>{name}</h2>
              <Link
                className='text-base-content text-opacity-40'
                to={`/user/${playertag}`}
              >
                Visit Profile
              </Link>
            </div>
          </div>
        </div>
      )
    }
UserItem.propTypes = {
    user: PropTypes.object.isRequired
}

export default UserItem