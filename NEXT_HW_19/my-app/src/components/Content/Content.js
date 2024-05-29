import styles from './Content.module.css';

const Content = (props) => {
    const { contents, deleteContent, editContent } = props;
    return (
        <div className={styles.container}>
            {contents.map((content) => (
                <div className={styles.container2} key={content.id}>
                    <div className={styles.title}>{content.title}</div>
                    <div className={styles.content}>{content.content}</div>
                    <div className={styles.control}>
                        <button className={styles.edit} onClick={() => deleteContent(content.id)}>
                            삭제
                        </button>
                        <button
                            className={styles.edit}
                            onClick={() => editContent(content.id, content.title, content.content)}
                        >
                            수정
                        </button>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default Content;
