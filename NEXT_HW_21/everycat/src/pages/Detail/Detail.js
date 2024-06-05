import { useEffect, useRef, useState } from 'react';
import { useParams } from 'react-router-dom';
import styles from './Detail.module.css';

const Detail = () => {
    const { id } = useParams();
    const catId = parseInt(id);
    const [cat, setCat] = useState(null);
    const [catUrl, setCatUrl] = useState('');
    const urlInputRef = useRef(null);

    useEffect(() => {
        const storedCatCategories = JSON.parse(localStorage.getItem('catCategories'));
        if (storedCatCategories) {
            const foundCat = storedCatCategories.find((cat) => cat.id === catId);
            if (foundCat) {
                setCat(foundCat);
                setCatUrl(foundCat.image);
            }
        }
    }, [catId]);

    if (!cat) {
        return <h1>존재하지 않는 고양이입니다.</h1>;
    }

    const changeCatUrl = () => {
        const newCatUrl = urlInputRef.current.value;
        if (newCatUrl) {
            setCatUrl(newCatUrl);

            const storedCatCategories = JSON.parse(localStorage.getItem('catCategories'));
            const newCatCategories = storedCatCategories.map((cat) => {
                if (cat.id === catId) {
                    return { ...cat, image: newCatUrl };
                }
                return cat;
            });
            localStorage.setItem('catCategories', JSON.stringify(newCatCategories));
        }
    };

    return (
        <div className={styles.box}>
            <h1 className={styles.name}>{cat.name}</h1>
            <img src={catUrl} alt={cat.name} />
            <p className={styles.description}>{cat.description}</p>
            <input type="text" ref={urlInputRef} placeholder="새로운 고양이 사진 주소"></input>
            <button onClick={changeCatUrl} className={styles.change}>
                내가 더 예쁜 고양이 사진을 찾았어요!
            </button>
        </div>
    );
};

export default Detail;
