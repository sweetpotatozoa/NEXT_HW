import styles from './Header.module.css';

const Header = (props) => {
    const { title } = props;
    return (
        <header className={styles.header}>
            <div className={styles.title}>{title}</div>
        </header>
    );
};

export default Header;
