import styles from './Home.module.css';
import { useNavigate } from 'react-router-dom';
import basicCatCategory from '../../catData/catData';
import { useEffect, useState } from 'react';

const Home = () => {
    const navigate = useNavigate();

    const navigateHandler = (id) => {
        navigate(`/detail/${id}`);
    };

    const [catCategory, setCatCategory] = useState([]);

    useEffect(() => {
        const storedCatCategories = JSON.parse(localStorage.getItem('catCategories'));
        if (storedCatCategories) {
            setCatCategory(storedCatCategories);
        } else {
            setCatCategory(basicCatCategory);
            localStorage.setItem('catCategories', JSON.stringify(basicCatCategory));
        }
    }, []);

    return (
        <div className={styles.background}>
            <div className={styles.catFace}>
                <div className={styles.nose}>고양이 종류</div>
                <div className={styles.mouse}>{''}</div>
                <div className={styles.mouse2}>{''}</div>
                <div className={styles.titles}>
                    {catCategory.map((cat) => (
                        <div key={cat.id} className={styles.title} onClick={() => navigateHandler(cat.id)}>
                            {cat.name}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Home;
