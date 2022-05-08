import pdb
from collections import defaultdict
import matplotlib.pyplot as plt

from survtrace.dataset import load_data
from survtrace.evaluate_utils import Evaluator
from survtrace.utils import set_random_seed
from survtrace.model import SurvTraceSingle
from survtrace.train_utils import Trainer
from survtrace.config import STConfig

# define the setup parameters
STConfig['data'] = 'support'

set_random_seed(STConfig['seed'])

hparams = {
    'batch_size': 64,
    'weight_decay': 1e-4,
    'learning_rate': 1e-3,
    'epochs': 20,
}

df, df_train, df_y_train, df_test, df_y_test, df_val, df_y_val = load_data(STConfig)

model = SurvTraceSingle(STConfig)

trainer = Trainer(model)
trainer.fit((df_train, df_y_train), (df_val, df_y_val))

evaluator = Evaluator(df, df_train.index)
evaluator.eval(model, (df_test, df_y_test))


