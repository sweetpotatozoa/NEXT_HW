import style from './Title.module.css';

const Title = (props) => {
    const { title, poemNum } = props;
    return (
        <div className={style.container}>
            <div className={style.title}>{title}</div>
            <div className={style.subTitle}>{poemNum}</div>
        </div>
    );
};

export default Title;
