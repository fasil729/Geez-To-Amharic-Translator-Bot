import { AiFillAudio } from "react-icons/ai";
import { FaCamera } from "react-icons/fa";
import { GoHistory } from "react-icons/go";
import { GrFavorite } from "react-icons/gr";
import { Link, Outlet,useLocation  } from "react-router-dom";
import { useTheme } from "../hooks/useTheme";


const Layout = () => {
  const location = useLocation();
  const currentPath = location.pathname;
  const { theme, toggleTheme } = useTheme();
  return (
    <div className="" style={{ background: theme === 'light' ? '#fff' : '#333', color: theme === 'light' ? '#000' : '#fff' }}>
      <Outlet/>
       {/* bottom navbar */}

<div className='flex justify-around b-navabar mt-20'>

<Link to="/" className={`
${currentPath==="/"? 'active':'link'}
`}>
<AiFillAudio size={24}/>
<p  className='label'>Chat</p>
</Link>

<Link to="/camera"  className={`
${currentPath==="/camera"?'active':'link'}
`}>
<FaCamera size={24}/>
<p  className='label'>Camera</p>
</Link>


<Link to="/history"  className={`
${currentPath==="/history"?'active':'link'}
`}>
<GoHistory size={24}/>
<p className='label'>Histroy</p>
</Link>

<Link to="/favourite"  className={`
${currentPath==="/favourite"?'active':'link'}
`}>
<GrFavorite size={24}/>
<p  className='label'>Favorite</p>
</Link>



</div>
    </div>
    );
}
 
export default Layout;