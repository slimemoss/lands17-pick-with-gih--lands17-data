import pickle
from pathlib import Path
from typing import Any, Callable

type T = Any
r'''pickle可能なオブジェクト
https://docs.python.org/ja/3/library/pickle.html#what-can-be-pickled-and-unpickled
'''


def clear_cache(path: Path):
    path.unlink(missing_ok=True)


def read_cache(path: Path, create_hook: Callable[[], T], clear_cache=False) -> tuple[T, bool]:
    r''' create_hookで作成したデータをキャッシュします。

    :param path: データの保存先パス(相対パスの場合は、Path().joinpath('cache_data')からの相対)
    :param create_hook: データを作成するためのフック関数
    :param clear_cache: キャッシュをクリアするかどうか(デフォルトはFalse)
    '''

    path = Path().joinpath('cache_data', path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    if clear_cache or not path.exists():
        # キャッシュをクリアするか、ファイルが存在しない場合は新しいオブジェクトを作成
        obj = create_hook()
        with open(path, 'wb') as f:
            pickle.dump(obj, f)
        ishit = False
    else:
        # ファイルが存在し、キャッシュがクリアされていない場合はキャッシュから読み込む
        with open(path, 'rb') as f:
            obj = pickle.load(f)
        ishit = True
    return obj, ishit
