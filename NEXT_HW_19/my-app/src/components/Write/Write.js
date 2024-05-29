import styles from './Write.module.css';

const Write = (props) => {
    const { setIsWriting } = props;
    return (
        <div className={styles.write}>
            <button className={styles.writeBtn} onClick={() => setIsWriting(1)}>
                글쓰기
            </button>
        </div>
    );
};

export default Write;
