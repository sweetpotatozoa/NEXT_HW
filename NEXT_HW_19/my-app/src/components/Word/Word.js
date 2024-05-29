import style from './Word.module.css';

const Word = (props) => {
    const { word, word2 } = props;
    return (
        <div className={style.container}>
            <div className={style.word}>{word}</div>
            <div className={style.word2}>{word2}</div>
        </div>
    );
};

export default Word;
