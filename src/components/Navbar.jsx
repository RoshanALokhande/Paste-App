import { NavbarData } from '../data/Navbar.jsx';
import { NavLink } from "react-router-dom";
const Navbar = () => {
    return (
        <div className="w-full h-[45px] flex justify-center items-center px-4 bg-gray-800 gap-x-5 text-white fixed top-0 left-0 z-50">
                {NavbarData.map((link, idx) => (
                    <NavLink
                    key={idx}
                    to={link.path}
                    className={({ isActive }) =>
                        isActive
                        ? "text-blue-500 font-semibold text-xl"
                        : "text-white font-medium text-xl"
                    }
                    >
                    {link.title}
                    </NavLink>
                ))}
            </div>
    )
}

export default Navbar