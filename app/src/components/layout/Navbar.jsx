import {FaDragon} from 'react-icons/fa'
import {Link} from 'react-router-dom'
import {useContext} from 'react'
import BSContext from '../../context/BSContext/BSContext'
import PropTypes from 'prop-types'

function Navbar({ title }) {
    const {clearUser} = useContext(BSContext)

    return (
      <nav className='navbar mb-12 shadow-lg bg-neutral text-neutral-content'>
        <div className='container mx-auto'>
          <div className='flex-none px-2 mx-2'>
            <FaDragon className='inline pr-2 text-3xl' />
            <Link to='/' onClick={clearUser} className='text-lg font-bold align-middle'>
              {title}
            </Link>
          </div>
  
          <div className='flex-1 px-2 mx-2'>
            <div className='flex justify-end'>
              <Link to='/' onClick={clearUser} className='btn btn-ghost btn-sm rounded-btn'>
                Home
              </Link>
              <Link to='/about' className='btn btn-ghost btn-sm rounded-btn'>
                About
              </Link>
            </div>
          </div>
        </div>
      </nav>
    )
  }

Navbar.defaultProps = {
    title: 'BrawlStars Stats',
}

Navbar.propTypes = {
    title: PropTypes.string
}

export default Navbar