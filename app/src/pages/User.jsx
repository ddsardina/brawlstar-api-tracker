import { FaUserFriends, FaUsers, FaUser} from 'react-icons/fa'
import {useContext} from 'react'
import {Link} from 'react-router-dom'
import BSContext from '../context/BSContext/BSContext'

function User() {
    const {user, clearUser} = useContext(BSContext)

    const {
        name,
        playertag,
        trophies,
        level,
        victories3v3,
        victoriesSolo,
        victoriesDuo,
        club
      } = user

  return (
    <> 
      <div className='w-full mx-auto lg:w-10/12'>
        <div className='mb-4'>
        <Link to='/' onClick={clearUser} className='btn btn-ghost'>
            Back To Search
        </Link>
        </div>

        <div className='grid grid-cols-1 xl:grid-cols-3 lg:grid-cols-3 md:grid-cols-3 mb-8 md:gap-8'>
        <div className='custom-card-image mb-6 md:mb-0'>
            <div className='rounded-lg shadow-xl card image-full'>
            <figure>
                <img src="https://www.kindpng.com/picc/m/256-2568642_brawl-stars-logo-brawl-stars-logo-png-transparent.png" alt='' />
            </figure>
            <div className='card-body justify-end'>
                <h2 className='card-title mb-0'>{name}</h2>
                <p>{playertag}</p>
            </div>
            </div>
        </div>

        <div className='col-span-2'>
            <div className='mb-6'>
            <h1 className='text-3xl card-title'>
              {name}
            </h1>
            <p></p>
            <div className='mt-4 card-actions'>
                <a
                href="https://supercell.com/en/news"
                target='_blank'
                rel='noreferrer'
                className='btn btn-outline'
                >
                Visit SuperCell News
                </a>
            </div>
            </div>

            <div className='w-full rounded-lg shadow-md bg-base-100 stats'>
            {club && (
                <div className='stat'>
                <div className='stat-title text-md'>Club Name</div>
                <div className='text-lg stat-value'>{club}</div>
                </div>
            )}
            {level && (
                <div className='stat'>
                <div className='stat-title text-md'>Level</div>
                <div className='text-lg stat-value'>{level}</div>
                </div>
            )}
            {trophies && (
                <div className='stat'>
                <div className='stat-title text-md'>Trophy Count</div>
                <div className='text-lg stat-value'>{trophies}</div>
                </div>
            )}
            </div>
        </div>
        </div>

        <div className='w-full py-5 mb-6 rounded-lg shadow-md bg-base-100 stats'>
        <div className='stat'>
            <div className='stat-figure text-secondary'>
            <FaUsers className='text-3xl md:text-5xl' />
            </div>
            <div className='stat-title pr-5'>3v3 Victories</div>
            <div className='stat-value pr-5 text-3xl md:text-4xl'>
            {victories3v3}
            </div>
        </div>

        <div className='stat'>
            <div className='stat-figure text-secondary'>
            <FaUserFriends className='text-3xl md:text-5xl' />
            </div>
            <div className='stat-title pr-5'>Duo Victoires</div>
            <div className='stat-value pr-5 text-3xl md:text-4xl'>
            {victoriesDuo}
            </div>
        </div>

        <div className='stat'>
            <div className='stat-figure text-secondary'>
            <FaUser className='text-3xl md:text-5xl' />
            </div>
            <div className='stat-title pr-5'>Solo Victories</div>
            <div className='stat-value pr-5 text-3xl md:text-4xl'>
            {victoriesSolo}
            </div>
        </div>
        </div>
      </div>
    </>
  )
}

export default User